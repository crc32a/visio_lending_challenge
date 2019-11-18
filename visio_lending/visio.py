import json
import os

def load_json(file_name):
    file_path = os.path.expanduser(file_name)
    fp = open(file_path,"r")
    jtext = fp.read()
    fp.close()
    obj = json.loads(jtext)
    return obj

def save_json(obj,file_name):
    file_path = os.path.expanduser(file_name)
    jtext = json.dumps(obj,indent=2)
    fp = open(file_path,"w")
    fp.write(jtext)
    fp.close()


class Person(object):
    def __init__(self, credit_score, state):
        self.credit_score=credit_score
        self.state = state

    def __str__(self):
        fmt = "Person{credit_score=%s stat=%s}"
        return fmt % (self.credit_score, self.state)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.credit_score == other.credit_score and \
               self.state == other.state
               

class Product(object):
    def __init__(self, name, interest_rate, disqualified):
        self.name = name
        self.interest_rate = interest_rate
        self.disqualified = disqualified

    def __str__(self):
        fmt = "Product{name=%s interest_rate=%s disqualified=%s}"
        return fmt % (self.name, self.interest_rate, self.disqualified)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and \
               self.interest_rate == other.interest_rate and \
               self.disqualified == self.disqualified

class RulesEngine(object):
    def runRules(self, person, product, rules):
        for rule in rules:
            condition = rule[0]
            cond_param = rule[1]
            action = rule[2]
            action_param = rule[3]

            #Test conbditions
            if condition == "always":
                self.run_action(person, product, action, action_param)

            if condition == "state=" and person.state == cond_param:
                self.run_action(person, product, action, action_param)

            if condition == "credit_score>=" and \
                person.credit_score >= cond_param:
                self.run_action(person, product, action, action_param)

            if condition == "credit_score<" and \
                person.credit_score < cond_param:
                self.run_action(person, product, action, action_param)

            if condition == "product=" and product.name == cond_param:
                self.run_action(person, product, action, action_param)


    def run_action(self,person,product,action, action_param):
        if action == "set_interest":
            product.interest_rate = action_param

        elif action == "add_interest":
            product.interest_rate += action_param

        elif action == "set_disqualified":
            product.disqualified = action_param

