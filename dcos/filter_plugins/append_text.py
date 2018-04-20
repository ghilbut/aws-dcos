from ansible import errors

def append_text(item, suffix):
  """
  Make object to string and append other value:
    {{ "text"|append(':suffix') }}
    -> text:suffix
  """
  return str(item) + suffix
 
class FilterModule(object):
  ''' A filter to append text after target item '''
  def filters(self):
    return { 'append_text': append_text }
