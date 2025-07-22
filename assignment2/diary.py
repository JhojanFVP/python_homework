# Task 1: Diary with file I/O and exception handling
import traceback

def main():
    try:
        with open('diary.txt', 'a') as f:
            prompt = "What happened today? "
            while True:
                line = input(prompt)
                f.write(line + '\n')
                if line.lower() == "done for now":
                    break
                prompt = "What else? "
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        stack = [f"File:{t[0]}, Line:{t[1]}, Func:{t[2]}, Msg:{t[3]}" for t in tb]
        print(f"Exception type: {type(e).__name__}")
        if str(e): print(f"Exception message: {e}")
        print(f"Stack trace: {stack}")

if __name__ == "__main__":
    main()
