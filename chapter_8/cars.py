# 8-14. car_infos: Write a function that stores information about a car_info in a diction­ ary. The function should always receive a manufacturer and a model name. It  should then accept an arbitrary number of keyword arguments. Call the func­ tion with the required information and two other name-value pairs, such as a  color or an optional feature. Your function should work for a call like this one: car_info = make_car_info('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was  stored correctly. 

def make_car_info(manufacturer, model_name, **car_info):
    """
    Stores information about a car_info in a dictionary.
    """
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    
    # for k,v in car_info.items():
    #     car_info[k] = v
    
    return car_info


car = make_car_info('subaru', 'outback', color='blue', tow_package='True')
print(car)