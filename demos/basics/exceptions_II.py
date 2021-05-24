def divide():

    try:

        op1 = (float(input("1º: ")))

        op2 = (float(input("2º: ")))

        print("Result: " + str(op1 / op2))

    except ValueError:

        print("Value invalid")

    except ZeroDivisionError:

        print("Cant divide by 0")

    # This will always be executed
    finally:

        print("Finished correctly")

divide()