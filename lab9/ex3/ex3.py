from text_file_merger import file_merger


file_paths = ['file1.txt', 'file2.txt']
output_path = 'merged_file.txt'
custom_separator = '/'

file_merger.merge_text_files(file_paths, output_path, separator=custom_separator)
print(f"Files merged successfully. Output file: {output_path}")
