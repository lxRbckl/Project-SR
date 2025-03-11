# import <


# >


class Steps:


   def __init__(self):
      """  """

      self.steps = []


   def addStep(self, command, text, parameters):
      """  """

      self.steps.append(

         {

            "command" : command,
            "text" : text,
            "parameters" : parameters

         }

      )