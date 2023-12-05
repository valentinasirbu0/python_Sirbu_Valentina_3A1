def merge_text_files(file_paths, output_path, separator='\n'):
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as input_file:
                    output_file.write(input_file.read())
                    output_file.write(separator)
            except FileNotFoundError:
                print(f"Warning: File not found - {file_path}")