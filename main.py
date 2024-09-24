import os
import importlib
import platform
from collections import Counter
from member import Member

child_dir = os.path.join(os.path.dirname(__file__), 'members')
member_count = 0

for filename in os.listdir(child_dir):
    member_count += 1
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"members.{filename[:-3]}"
        importlib.import_module(module_name)

subclasses = Member.__subclasses__()
instances = [subclass() for subclass in subclasses]

average_age = sum([member.age for member in instances]) / (member_count - 1)
most_popular_major = Counter([member.major.name for member in instances]).most_common(1)[0][0]

os.system('cls' if platform.system() == "Windows" else 'clear')
print(f"The average age of the club members is: {average_age}")
print(f"The most popular major is: {most_popular_major}")
for member in instances:
    print(f"\n{member.name}:")
    member.intro()
