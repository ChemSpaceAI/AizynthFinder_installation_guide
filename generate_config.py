import yaml
import os

def generate_config(models_dir):
    template_path = 'template_config.yml'
    output_path = os.path.join(models_dir, 'custom_config.yml')

    with open(template_path, 'r') as f:
        config = yaml.safe_load(f)

    # Update paths in the config
    config['expansion']['uspto'] = [os.path.join(models_dir, 'Data/uspto_model.onnx'), os.path.join(models_dir, 'Data/uspto_templates.csv.gz')]
    config['filter']['uspto'] = os.path.join(models_dir, 'Data/uspto_filter_model.onnx')
    config['stock']['chemspace'] = os.path.join(models_dir, 'Data/chemspace_stock.hdf5')
    config['stock']['zinc'] = os.path.join(models_dir, 'Data/zinc_stock.hdf5')

    with open(output_path, 'w') as f:
        yaml.dump(config, f)

    print(f'Config file generated: {output_path}')

if __name__ == '__main__':
    current_directory = os.getcwd()
    generate_config(current_directory)
