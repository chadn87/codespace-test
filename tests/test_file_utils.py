import unittest
from src.utils.file_utils import get_files_in_directory
from unittest.mock import patch, mock_open, MagicMock

class TestGetFilesInDirectory(unittest.TestCase):
    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_non_recursive_all_files(self, mock_listdir, mock_isdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = ['file1.txt', 'file2.jpg', 'dir1']
        
        with patch('os.path.isfile', side_effect=lambda x: x != '/path/to/directory/dir1'):
            files = get_files_in_directory('/path/to/directory', recursive=False)
            self.assertEqual(files, [
                '/path/to/directory/file1.txt',
                '/path/to/directory/file2.jpg'
            ])
    
    @patch('os.path.isdir')
    @patch('os.walk')
    def test_recursive_with_extensions(self, mock_walk, mock_isdir):
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ('/path/to/directory', ('subdir1',), ('file1.txt', 'file2.jpg')),
            ('/path/to/directory/subdir1', (), ('file3.txt', 'file4.csv')),
        ]
        
        files = get_files_in_directory('/path/to/directory', recursive=True, extensions=['.txt'])
        self.assertEqual(files, [
            '/path/to/directory/file1.txt',
            '/path/to/directory/subdir1/file3.txt'
        ])
    
    @patch('os.path.isdir')
    def test_invalid_directory(self, mock_isdir):
        mock_isdir.return_value = False
        with self.assertRaises(ValueError):
            get_files_in_directory('/invalid/directory')
    
    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_non_recursive_with_extensions(self, mock_listdir, mock_isdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = ['file1.txt', 'file2.jpg', 'file3.txt']
        
        with patch('os.path.isfile', return_value=True):
            files = get_files_in_directory('/path/to/directory', recursive=False, extensions=['.txt'])
            self.assertEqual(files, [
                '/path/to/directory/file1.txt',
                '/path/to/directory/file3.txt'
            ])
    
    @patch('os.path.isdir')
    @patch('os.walk')
    def test_recursive_no_extensions(self, mock_walk, mock_isdir):
        mock_isdir.return_value = True
        mock_walk.return_value = [
            ('/path/to/directory', ('subdir1',), ('file1.txt', 'file2.jpg')),
            ('/path/to/directory/subdir1', (), ('file3.txt', 'file4.csv')),
        ]
        
        files = get_files_in_directory('/path/to/directory', recursive=True)
        self.assertEqual(files, [
            '/path/to/directory/file1.txt',
            '/path/to/directory/file2.jpg',
            '/path/to/directory/subdir1/file3.txt',
            '/path/to/directory/subdir1/file4.csv'
        ])

if __name__ == '__main__':
    unittest.main()
