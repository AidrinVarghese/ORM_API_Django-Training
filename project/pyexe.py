# def my_functions(arg):
#     try:
#         x = 5 + arg        
#         # print(x)
#     except Exception as e:
#         print("Exp !", e)
#         # x = None
#         return None
#     finally:
#         return
# a = my_functions("sss")
# print(a)

def my_functions(arg):
    try:
        x = {"name": "john", "age": "20"}        
        answer = 15 / 0
        result = x[arg]
        
    except KeyError as k:
        print("Invalid key entered:", k)
        result = "Demo name"
    
    except ZeroDivisionError:
        print("Division by zero")
        result = 0
    except Exception as e:
        print("Exception:", e)
        result = None
    finally:
        return result

a = my_functions("age")
print(a)
 
    