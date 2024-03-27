# class Model:
#     class __metaclass__(type):
# #         def __init__(self, name, type, other):
#         def __new__(cls, name, bases, dct):
#             dct['_fields'] = {}
#             for attr_name, attr_value in dct.items():
#                 dct['_fields'][attr_name] = attr_value.upper()  # Example modification: convert string attributes to uppercase
#                 del dct[attr_name]
#             return super().__new__(cls, name, bases, dct)

#     def validate(self):
#         return all(var.validate() for name,var in dir(self).items())

# class User(Model):
#     first_name = 2 #CharField(max_length=30, default='Adam')
#     # last_name = CharField(max_length=50)
            
# print(hasattr(User, 'first_name'))
# print(User.__metaclass__)

class InterceptAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        intercepted_attributes = {}

        # Intercept the creation of class attributes
        for attr_name, attr_value in dct.items():
            # Modify the attribute value or behavior here
            if isinstance(attr_value, str):
                # Store the original attribute under a modified name
                intercepted_attributes[attr_name + '_modified'] = attr_value.upper()

        # Remove the original attributes from the class dictionary
        for original_attr_name in intercepted_attributes.keys():
            del dct[original_attr_name[:-9]]  # Remove the original attribute
        
        # Add the intercepted attributes to the class dictionary
        dct.update(intercepted_attributes)
        
        # Create the class with modified attributes
        return super().__new__(cls, name, bases, dct)


# Example usage
class M(metaclass=InterceptAttributesMeta):
    # __metaclass__ = InterceptAttributesMeta
    pass

class A:
    pass
class MyClass(M):
    firstname = "value1"
    attribute2 = "value2"

print(hasattr(MyClass, 'firstname'))  # Output: False
print(hasattr(MyClass, 'attribute1_modified'))  # Output: True
print(type(A))