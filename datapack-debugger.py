import sys
import os
import shutil

def mkdir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass

def find_replace(filename, str1, str2):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(str1, str2)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

if __name__ == "__main__":
    #Command line parsing
    if len(sys.argv) == 1:
        print("Error: No data pack specified")
        exit(1)
    try:
        o_flag = sys.argv.index("-o")
        output = sys.argv[o_flag+1]
    except ValueError:
        #Runs when there is no -o
        if len(sys.argv) > 2:
            print("Error: Too many arguments")
            exit(1)
        datapack = sys.argv[1]
        output = datapack + "-debug"
    except IndexError:
        #Runs when there is -o but no other argument
        print("Error: No output path specified")
        exit(1)
    else:
        if len(sys.argv) == 3:
            print("Error: No data pack specified")
            exit(1)
        elif len(sys.argv) > 4:
            print("Error: Too many arguments")
            exit(1)
        args = sys.argv[1:]
        args.remove("-o")
        args.remove(sys.argv[o_flag+1])
        datapack = args[0]
    
    if os.path.isdir(output):
        shutil.rmtree(output)
    print(f"Copying data pack to {output}")
    shutil.copytree(datapack,output)
    data_dir = os.path.join(output, "data")
    print(f"Data directory: {data_dir}")
    namespaces = [os.path.join(data_dir, i) for i in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, i))]
    print("Namespaces found:", *namespaces)
    for i in namespaces:
        for root, dirs, files in os.walk(os.path.join(i, "functions")):
            for file in files:
                filename = os.path.join(root,file)
                print(f"Replacing players in file {filename}")
                find_replace(filename, "@p[", "@e[sort=nearest,limit=1,tag=fake_player,")
                find_replace(filename, "@a[", "@e[tag=fake_player,")
                find_replace(filename, "@r[", "@e[sort=random,limit=1,tag=fake_player,")
                find_replace(filename, "@p", "@e[sort=nearest,limit=1,tag=fake_player]")
                find_replace(filename, "@a", "@e[tag=fake_player]")
                find_replace(filename, "@r", "@e[sort=random,limit=1,tag=fake_player]")
                find_replace(filename, "tellraw @e", "tellraw @a")
    print("Done\n")
