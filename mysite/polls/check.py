from river.models.hook import BEFORE, AFTER

def _handle_my_transitions(hook):
    workflow = hook['payload']['workflow']
    workflow_object = hook['payload']['workflow_object']
    source_state = hook['payload']['transition_approval'].meta.source_state
    destination_state = hook['payload']['transition_approval'].meta.destination_state
    last_approved_by = hook['payload']['transition_approval'].transactioner
    if hook['when'] == BEFORE:
        print('A transition from %s to %s will soon happen on the object with id:%s and field_name:%s!' % (source_state.label, destination_state.label, workflow_object.pk, workflow.field_name))
    elif hook['when'] == AFTER:
        print('A transition from %s to %s has just happened on the object with id:%s and field_name:%s!' % (source_state.label, destination_state.label, workflow_object.pk, workflow.field_name))
    print('Who approved it lately is %s' % last_approved_by.username)

def _handle_my_approvals(hook):
    workflow = hook['payload']['workflow']
    workflow_object = hook['payload']['workflow_object']
    approved_by = hook['payload']['transition_approval'].transactioner
    if hook['when'] == BEFORE:
        print('An approval will soon happen by %s on the object with id:%s and field_name:%s!' % ( approved_by.username, workflow_object.pk, workflow.field_name ))
    elif hook['when'] == AFTER:
        print('An approval has just happened by %s  on the object with id:%s and field_name:%s!' % ( approved_by.username, workflow_object.pk, workflow.field_name ))

def _handle_completions(hook):
    workflow = hook['payload']['workflow']
    workflow_object = hook['payload']['workflow_object']
    if hook['when'] == BEFORE:
        print('The workflow will soon be complete for the object with id:%s and field_name:%s!' % ( workflow_object.pk, workflow.field_name ))
    elif hook['when'] == AFTER:
        print('The workflow has just been complete for the object with id:%s and field_name:%s!' % ( workflow_object.pk, workflow.field_name ))

def handle(context):
    hook = context['hook']
    if hook['type'] == 'on-transit':
        _handle_my_transitions(hook)
    elif hook['type'] == 'on-approved':
        _handle_my_approvals(hook)
    elif hook['type'] == 'on-complete':
        _handle_completions(hook)
    else:
        print("Unknown event type %s" % hook['type'])