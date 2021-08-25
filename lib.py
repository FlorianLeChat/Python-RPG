# Try to check if the input is a number
# Source : https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def tryNumber(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
