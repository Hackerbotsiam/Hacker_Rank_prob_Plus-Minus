# Plus Minus
def plusMinus(arr):
    array_len=len(arr) # Total length of array
    positive_count=sum(1 for x in arr if x>0)
    negative_count=sum(1 for x in arr if x<0)
    zero_count=sum(1 for x in arr if x==0)
    ###########
    ratio_positive= positive_count / array_len
    ratio_negative= negative_count / array_len
    ratio_zero= zero_count / array_len
    #######
    print(f"{ratio_positive:.6f}")
    print(f"{ratio_negative:.6f}")
    print(f"{ratio_zero:.6f}")

if __name__=="__main__":
    n=int(input()) # Enter the how many numbers you want
    arr=list(map(int,input().split())) # Enter the valus
    # functio call
    plusMinus(arr)