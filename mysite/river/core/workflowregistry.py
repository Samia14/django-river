class WorkflowRegistry(object):
    def __init__(self):
        self.workflows = {}
        self.class_index = {}

    def add(self, name, cls):
        print("in work flow registry ",name)
        print("in wor flow registry ",cls)
        self.workflows[id(cls)] = self.workflows.get(id(cls), set())
        self.workflows[id(cls)].add(name)
        print("some thing of anme",name)
        print("workflow,",self.workflows)
        self.class_index[id(cls)] = cls

    def get_class_fields(self, model):
        print("in work flow registry with get class field",self.workflows[id(model)],self.workflows)
        return self.workflows[id(model)]


workflow_registry = WorkflowRegistry()
