'''
Module package for sky catalogue simulation
'''

def func():
	print("You just ran the function called 'func' from module 'mymodule'")

if __name__ == "__main__":
	print("Hello from module 'mymodule'")
else:
	print(f"You imported the module, __name__ = ",__name__)
__all__ = ['sky_sim']
