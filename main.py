from app import task_1, task_2, task_4, task_3
import sys

def main():
    save_file = False
    save_path = ''
    sec_arg = ["-medals", "-total", "-overall", "-interactive"]
    medals =["Gold", "Silver", "Bronze"] 

    if sys.argv[1] not in sec_arg:
        print("Error: The '-medals/overall/total/interactive' argument must be the second argument.")
        sys.exit(1)

    if len(sys.argv) == 6 and sys.argv[4] == '-output':
        save_file = True
        save_path = sys.argv[5]

    if sys.argv[1] == sec_arg[0]:
        task_1(save_file, save_path)

    elif sys.argv[1] == sec_arg[1] and int(sys.argv[2]) >= 1896 and int(sys.argv[2]) <= 2016:
        task_2(medals)

    elif sys.argv[1] == sec_arg[2]:
        task_3(medals)

    elif sys.argv[1] == sec_arg[3]:
        task_4(medals)


if __name__ == "__main__":
    main()
