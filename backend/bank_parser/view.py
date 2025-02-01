from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .parsers.chase.chase_parser import ChaseParser
from .utils.file_handlers import handle_uploaded_file, get_file_type
import os


class BankStatementUpload(APIView):
    def post(self, request):
        # Get uploaded file
        file_obj = request.FILES["file"]
        file_path = handle_uploaded_file(file_obj)

        # Identify and parse
        if ChaseParser.identify(file_path):
            file_type = get_file_type(file_path)

            if file_type == "pdf":
                transactions = ChaseParser.parse_pdf(file_path)
            elif file_type == "csv":
                transactions = ChaseParser.parse_csv(file_path)
            else:
                return Response(
                    {"error": "Unsupported file type"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Save transactions (example)
            for t in transactions:
                Transaction.objects.create(
                    user=request.user,
                    date=t["date"],
                    description=t["description"],
                    amount=t["amount"],
                    bank_name="Chase",
                )

            os.remove(file_path)  # Cleanup
            return Response({"message": f"Processed {len(transactions)} transactions"})

        return Response(
            {"error": "Unsupported bank format"}, status=status.HTTP_400_BAD_REQUEST
        )
