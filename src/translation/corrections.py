class Corrections:
    def remove_duplicates(method):
        def function(*args, **kwargs):
            result = method(*args, **kwargs)
            text = args[1]
            if (
                text.count(" ") == 0 or (text.count(" ") == 1 and text.endswith(" "))
            ) and result.find(" "):
                result = result.split(" ")[0]
            return result

        return function
