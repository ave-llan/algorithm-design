
function sumOfMaxSubarray (a) {
  var maxAll = a[0], maxRight = a[0]
  for (var i = 1; i < a.length; i++) {
    maxRight = Math.max(maxRight + a[i], a[i])
    maxAll   = Math.max(maxRight, maxAll)
  }
  return maxAll
}

test = [5, -5, 2, 3, -10, 1, 2, -3, 20, -50, 19, 1, 1]
console.log(sumOfMaxSubarray(test))
