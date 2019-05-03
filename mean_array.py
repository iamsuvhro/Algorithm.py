def _sum_(n,arr):
    return(sum(arr))
def mean(arr):
    idx= len(arr)
    sums=_sum_(idx,arr)
    mean =  sums / (arr[0]+arr[idx-1])
    return mean
