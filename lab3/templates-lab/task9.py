import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open('data-task9.yml') as f:
   data = yaml.safe_load(f)

# Load Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template-task9.j2')

# Generate config for each router
for router in data['routers']:
   config = template.render(router=router)
   filename = f"{router['name']}_config.txt"
   with open(filename, 'w') as f:
       f.write(config)
   print(f"Configuration for {router['name']} written to {filename}")
