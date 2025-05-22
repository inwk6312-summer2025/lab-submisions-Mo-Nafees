from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task5.j2")

inter_list = [
"GigabitEthernet0/1",
"GigabitEthernet0/2",
"GigabitEthernet0/3"
]

print(template.render(interface_list=inter_list))

from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task5a.j2")

inter_dict = {
"GigabitEthernet0/1": "Server port number one",
"GigabitEthernet0/2": "Server port number two",
"GigabitEthernet0/3": "Server port number three"
}
print(template.render(interface_dict=inter_dict))
