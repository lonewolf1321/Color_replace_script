import os
import re
import colorsys

input_directory = "/home/nobody/Documents/dialer"
output_directory = "/home/nobody/Documents"


print("Input directory:", input_directory)
print("Output directory:", output_directory)
print("Input directory contents:", os.listdir(input_directory))

def generate_target_colors(original_colors):
    hues = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
    target_colors = []
    invalid_colors = []

    for color in original_colors:
        if len(color) == 9:
            try:
                hex_to_rgb = lambda h: (int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16))
                rgb_color = hex_to_rgb(color)
                hsv_color = colorsys.rgb_to_hsv(*rgb_color)
                hue = hsv_color[0] * 360

                closest_hue_index = round((hue - min(hues)) / (max(hues) - min(hues)))
                closest_hue = hues[closest_hue_index]

                rgb_color = colorsys.hsv_to_rgb(closest_hue / 360, hsv_color[1], hsv_color[2])
                target_color = "#{:02x}{:02x}{:02x}".format(int(255 * rgb_color[0]), int(255 * rgb_color[1]), int(255 * rgb_color[2]))
                target_colors.append(target_color[:9])  # Only keep the first 9 digits
            except (ValueError, IndexError):
                invalid_colors.append(color)
                target_colors.append(color)
        else:
            target_colors.append(color)

    return target_colors, invalid_colors

def replace_colors(file_path):
    print("Processing file:", file_path)
    print("Reading file content...")
    with open(file_path, 'r') as f:
        original_content = f.read()

    original_colors = re.findall(r"#[0-9a-fA-F]{6,8}", original_content)

    print("Found original colors:", original_colors)

    # Generate target colors and get invalid colors
    target_colors, invalid_colors = generate_target_colors(original_colors)

    print("Generated target colors:", target_colors)
    print("Invalid colors:", invalid_colors)

    file_content = original_content
    for original_color, target_color in zip(original_colors, target_colors):
        file_content = file_content.replace(original_color[:9], target_color[:9])

    print("Modified file content:\n", file_content)

    # Save the modified XML files to the output_directory
    file_name = os.path.basename(file_path)  # Get the file name from the original path
    output_file_path = os.path.join(output_directory, file_name)  # Construct the output path

    print("Saving modified file to:", output_file_path)
    with open(output_file_path, 'w') as f:
        f.write(file_content)

    print("Modified file saved successfully.")

def process_directory(directory_path):
    print("Processing directory:", directory_path)
    for entry in os.scandir(directory_path):
        if entry.is_file():
            if entry.name == "colors.xml":
                replace_colors(entry.path)
        elif entry.is_dir(follow_symlinks=False):
            process_directory(entry.path)

# Process colors.xml files in the input_directory and its subdirectories
print("Starting to process input directory...")
process_directory(input_directory)
