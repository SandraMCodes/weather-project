import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):

   
    isoformat_date = datetime.isoformat

    isoformat_date = datetime.fromisoformat(iso_string)

    return (isoformat_date.strftime("%A %d %B %Y"))
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    


def convert_f_to_c(temp_in_fahrenheit):
    converted = float(temp_in_fahrenheit)
    f_to_c = (converted - 32) * 5 / 9
    rounded = round(f_to_c,1)
    return rounded

#    tempf = float(input('Fahrenheit? '))
#    tempc = convert_f_to_c(tempf)
#    print(f'{tempc:.1f} degC')
    """Converts a temperature from Fahrenheit to Celcius.

   

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    


def calculate_mean(weather_data):
    weather_data_float = [float(i) for i in weather_data]
    return float(sum(weather_data_float)/len(weather_data_float))
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    


def load_data_from_csv(csv_file):
    csv_list =[]
    with open(csv_file) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader: 
            if row:
                sub_list =[]
                sub_list.append(row[0])
                sub_list.append(float (row[1]))
                sub_list.append(float (row[2]))
                print(sub_list) 
                csv_list.append(sub_list) 
    return csv_list
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:    
        min_temp = float(min(weather_data))
        for index, value in enumerate(weather_data):
            if float (value) == min_temp:
                min_temp_index = index
        return min_temp, min_temp_index
    else:
        return ()



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:    
        max_temp = float(max(weather_data))
        for index, value in enumerate(weather_data):
            if float (value) == max_temp:
                max_temp_index = index
        return max_temp, max_temp_index
    else:
        return ()


def generate_summary(weather_data):
    
    #combine string with a variable value
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    minValue = 0
    maxValue = 0
    minDate = ""
    maxDate = ""
    numberOfDays=len(weather_data)
    sumLowTemp = 0
    sumHighTemp = 0

    for value in weather_data:
        if minValue == 0: 
            minValue = value[1]
            maxValue = value[2]
            minDate = value[0]
            maxDate = value[0]
        if minValue > value[1]: 
            minValue = value[1]
            minDate = value[0]
        if maxValue < value[2]: 
            maxValue = value[2] 
            maxDate = value[0]
        sumLowTemp = sumLowTemp+value[1] 
        sumHighTemp = sumHighTemp+value[2]
    
    finalMinDate = convert_date(minDate)
    finalMaxDate = convert_date(maxDate)
    finalMinTemp = str(convert_f_to_c(minValue))
    finalMaxTemp = str(convert_f_to_c(maxValue))
    averageLowTemp = str(convert_f_to_c(sumLowTemp/numberOfDays)) ##Calculate the average of low temps and convert from a float to a String
    averageHighTemp = str(convert_f_to_c(sumHighTemp/numberOfDays)) ## Calculate the average of high temps and convert from a float to a String

    ## Concatenate variables and strings together to make the required output.
    summaryOutput = str(numberOfDays)+" Day Overview\n  The lowest temperature will be "+finalMinTemp+"°C, and will occur on "+finalMinDate+".\n"
    summaryOutput = summaryOutput + "  The highest temperature will be "+finalMaxTemp+"°C, and will occur on "+finalMaxDate+".\n"
    summaryOutput = summaryOutput + "  The average low this week is "+averageLowTemp+"°C.\n"
    summaryOutput = summaryOutput + "  The average high this week is "+averageHighTemp+"°C.\n"

    return summaryOutput

    ##temperatures = [data[1] for data in weather_data]
    ##mean_temp = calculate_mean(temperatures)
    ##min_temp, min_temp_index = find_min(temperatures)
    ##max_temp, max_temp_index = find_max(temperatures)

    ##min_date = convert_date(weather_data[min_temp_index][0])
    ##max_date = convert_date(weather_data[max_temp_index][0])

    ##summary = (f"Weather Summary:\n"
               ##f"Mean Temperature: {format_temperature(mean_temp)}\n"
               ##f"Minimum Temperature: {format_temperature(min_temp)} on {min_date}\n"
               ##f"Maximum Temperature: {format_temperature(max_temp)} on {max_date}")
    
    ##return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    outputValue=""
        
    for value in weather_data:
        minTempInC = convert_f_to_c(value[1]) 
        maxTempInC = convert_f_to_c(value[2]) 
        outputValue = outputValue + f"---- "+convert_date(value[0])+" ----\n  Minimum Temperature: "+str(minTempInC)+"°C\n  Maximum Temperature: "+str(maxTempInC)+"°C\n\n"
        minTempInC = None
        maxTempInC = None

    return outputValue

    ##daily_summaries = []
    ##for day_data in weather_data:
        ##date_str = convert_date(day_data[0])
        ##temp_c = convert_f_to_c(day_data[1])
        ##daily_summary = (f"Date: {date_str}\n"
                         ##f"Temperature: {format_temperature(temp_c)}\n"
                         ##f"Humidity: {day_data[2]}%")
        ##daily_summaries.append(daily_summary)
    
    ##return "\n\n".join(daily_summaries)
    

##def main():
    ##csv_file_path = 'weather_data.csv'
    ##weather_data = load_data_from_csv(csv_file_path)
    ##summary = generate_summary(weather_data)
    ##print("Overall Weather Summary:")
    ##print(summary)
    ##print("\n" + "="*40 + "\n")
    ##daily_summary = generate_daily_summary(weather_data)
    ##print("Daily Weather Summaries:")
    ##print(daily_summary)


##if __name__ == "__main__":
    ##main()

