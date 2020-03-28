#utility function file
#function to return five links (maximum)
def get_top_five_link(result):
    count=0
    results=[]
    print(len(result))
    for count in range(len(result)):
        if count<5:
            results.append(result[count]['link'])
            count=count+1
        else:
            break

    return results