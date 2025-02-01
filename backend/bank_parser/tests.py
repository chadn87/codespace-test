from django.test import TestCase
from .parsers.chase.test_chase_parser import ChaseParserTests

# Re-export your existing tests
__test__ = {
    'ChaseParserTests': ChaseParserTests
}
