#passing value to operation module

import module

module.add(10,5)
module.sub(10,5)


## approach 2

from module import add,sub

add(10,5)
sub(10,5)

##approach 3

from module import *  # * means all

add(10,5)
sub(10,5)