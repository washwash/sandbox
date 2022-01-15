from typing import List
from collections.abc import Callable

class Knowledge:

    def __init__(self, fact: str, secret_condition: Callable = None):
        self.fact = fact
        self.secret_condition = secret_condition

    def __str__(self):
        return self.fact

    def is_secret(self):
        if self.secret_condition:
            return self.secret_condition()


class KnowledgeGenerator:
    def __init__(self, knowledge):
        self._knowledge = knowledge

    def __iter__(self):
        generate = (
            knowledge for knowledge in self._knowledge
            if not knowledge.is_secret()
        )
        return iter(generate)

class Person:
    def __init__(self, knowledge: List[Knowledge] = None):
        self.knowledge = self.init_knowledge(knowledge) if knowledge else []
        self._hits_count = 0

    def init_knowledge(self, knowledge: List[Knowledge]):
        self.knowledge = KnowledgeGenerator(knowledge)

    def enough_hits(self, hits: int):
        def f():
            return self._hits_count < hits
        return f

    def kick(self):
        self._hits_count += 1


oleg = Person()

info_name = Knowledge("my name is Oleg")
info_age = Knowledge("I'm 12 years old")
secret_penis_length = Knowledge("penis is 5 сm", oleg.enough_hits(3))

oleg.init_knowledge([
    info_name,
    info_age,
    secret_penis_length
])


for k in oleg.knowledge:
    print(k)

oleg.kick()
oleg.kick()
oleg.kick()

for k in oleg.knowledge:
    print(k)
