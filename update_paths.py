import json
import pandas as pd

print("开始更新数据文件中的图像路径...")

# 更新JSON文件
print("更新JSON文件...")
try:
    # 读取JSON文件
    with open('data/camera_data_cleaned.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 更新图像路径
    for camera in data:
        if 'image_file' in camera and camera['image_file'] and isinstance(camera['image_file'], str) and camera['image_file'].startswith('images/'):
            camera['image_file'] = 'data/' + camera['image_file']

    # 保存更新后的JSON文件
    with open('data/camera_data_cleaned.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("JSON文件更新成功！")
except Exception as e:
    print(f"更新JSON文件时出错: {str(e)}")

# 更新CSV文件
print("更新CSV文件...")
try:
    # 读取CSV文件
    df = pd.read_csv('data/camera_data_cleaned.csv')

    # 更新图像路径
    df['image_file'] = df['image_file'].apply(
        lambda x: 'data/' + x if isinstance(x, str) and x.startswith('images/') else x
    )

    # 保存更新后的CSV文件
    df.to_csv('data/camera_data_cleaned.csv', index=False)
    
    print("CSV文件更新成功！")
except Exception as e:
    print(f"更新CSV文件时出错: {str(e)}")

print("路径更新完成！") 