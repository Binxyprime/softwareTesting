from nose2.events import Plugin


class ReqTracer(Plugin):
    configSection = 'req-tracer'


    def afterSummaryReport(self,event):
        outputFile = open("Project_Traces.txt", "w")
        for key, item in sorted(Requirements.items()):
            outputFile.write(key+' ')
            for func in item.func_name:
                outputFile.write(func+', ')
            outputFile.write('\n')
        for job in Stories:
            outputFile.write(job.js_text+' ')
            for func in job.func_name:
                outputFile.write(func+', ')
            outputFile.write('\n')

class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []

class JSTrace(object):
    js_text = ""

    def __init__(self, text):
        self.js_text = text
        self.func_name = []

Requirements = {}
Stories = []

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


# ***********************************************************************
#                       JobStoryTrace
# ***********************************************************************

def story(job_story):
    def wrapper(func):
        def add_job_and_call(*args, **kwargs):
            for job in Stories:
                if job.js_text == job_story.lower().strip():
                    job.func_name.append(func.__name__)
                    break
            else:
                raise Exception('Story not found {}'.format(job_story))
            return func(*args, **kwargs)

        return add_job_and_call

    return wrapper


# *****************************************************
#                   open
# *****************************************************
with open('requirementTest.txt') as f:
    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
        if '*' in line:
            line = line.lower()
            line = line.strip()
            desc = line.split(' ', 1)[1]
            Stories.append(JSTrace(desc))
