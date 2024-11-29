import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_voxelshape_code(json_data):
    voxel_shapes = []
    result=[]
    for idx, element in enumerate(json_data['elements']):
        from_coords = element['from']
        to_coords = element['to']
        shape_code = f"public static final VoxelShape SHAPE{idx + 1} = Block.box({from_coords[0]}D, {from_coords[1]}D, {from_coords[2]}D, {to_coords[0]}D, {to_coords[1]}D, {to_coords[2]}D);"
        voxel_shapes.append(shape_code)
    return voxel_shapes

def generate_combined_voxelshape(voxel_shapes):
    combined_code = "public static final VoxelShape SHAPE =  Shapes.or(" + ", ".join([f"SHAPE{i+1}" for i in range(len(voxel_shapes))]) + ");"
    return combined_code

def main():
    json_data = read_json('origin.json') #json文件的路径
    voxel_shapes = generate_voxelshape_code(json_data)

    for shape in voxel_shapes:
        print(shape)

    combined_voxelshape = generate_combined_voxelshape(voxel_shapes)
    print(combined_voxelshape)

if __name__ == '__main__':
    main()