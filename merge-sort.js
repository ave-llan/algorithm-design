function mergeSort (array, isOrderedBefore) {
  if (array.length <= 1) {
    return array
  }

  var mid = Math.floor(array.length / 2)
  return merge(
    mergeSort(array.slice(0, mid), isOrderedBefore), 
    mergeSort(array.slice(mid)   , isOrderedBefore),
    isOrderedBefore
  )

}

function merge (a, b, isOrderedBefore) {
  var merged = [], i = 0, j = 0
  while (i < a.length && j < b.length) {
    if (isOrderedBefore(a[i], b[j])) {
      merged.push(a[i])
      i += 1
    } else {
      merged.push(b[j])
      j += 1
    }
  }
  // add any leftover
  merged = merged.concat(a.slice(i))
  merged = merged.concat(b.slice(j))
  return merged
}

var test = [6,1,2,3,2,12, 1, -5, 3, 6]

var sorted = mergeSort(test, (a, b) => a < b)
console.log(sorted)