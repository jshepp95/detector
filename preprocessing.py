import os
import cv2

dir = "data/imgs/raw"

prefix = "img"

files = sorted([f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))])
img_sizes = []

print(f"Restructuring {len(files)} samples ... ")

for idx, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1].lower()

    if ext in {".jpg", ".jpeg", ".png"}:
        img_path = os.path.join(dir, filename)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping {filename} (could not load)")
            continue

        h, w, _ = img.shape
        img_sizes.append((w, h))

        new_filename = f"{prefix}_{idx:03d}.jpg"
        new_path = os.path.join(dir, new_filename)

        os.rename(img_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print(">> Restructured Raw Files ... ")

### ANALYZE IMAGE SIZES ###
widths, heights = zip(*img_sizes)

min_width, max_width = min(widths), max(widths)
min_height, max_height = min(heights), max(heights)

avg_width = sum(widths) // len(widths)
avg_height = sum(heights) // len(heights)

print("\n>> IMAGE SIZE ANALYSIS:")
print(f"Min size: {min_width}x{min_height}")
print(f"Max size: {max_width}x{max_height}")
print(f"Avg size: {avg_width}x{avg_height}")

### TEMPLATE SIZE ###
recommended_size = (min(avg_width, avg_height) // 4, min(avg_width, avg_height) // 4)

print(f"\nRecommended template size: {recommended_size[0]}x{recommended_size[1]}")

with open("data/image_size_log.txt", "w") as f:
    f.write(f"Min size: {min_width}x{min_height}\n")
    f.write(f"Max size: {max_width}x{max_height}\n")
    f.write(f"Avg size: {avg_width}x{avg_height}\n")
    f.write(f"Recommended template size: {recommended_size[0]}x{recommended_size[1]}\n")

