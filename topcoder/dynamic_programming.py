import sys; sys.path.insert(0, '/Users/henry/Dropbox/dev/practice/datastructs')
import sorting, math

class OrderOfOperations:

    def minTime(self, s):
        """  Dynamic programming problem
        https://community.topcoder.com/stat?c=problem_statement&pm=13987

        Constraints:
          n = [1, 50]
          m = [1, 20]
          n total instructions (len(s))
          instruction has m characters, 0s or 1s

          010101
          110001
          000111
          010010
          100011

        Just thoughts: 
          - knapsack problem with no weights
          - value -> the runtime, as small as possible
          - weight -> ? what are the constraints?
          - Intuitively, we want every new memory access to be as minimal as possible
            per instruction
          - Initially, every instruction will be at their maximum values. With 
            each one taken, the rest's values will decrease.
            - all-zero instructions will cost nothing at all times. single-1's
              will always cost 1 or zero. 
              Is it ever justified to choose a two-1 in order to make a single-1
              0? That means take a value hit of 4 over taking a 2 for the two singles
              it removes. so never

          - intuititvely, best solution is to do all single instructions first. 

          
          FINAL SOLUTION: First sort all instructions from most to least. 
          Then do the basic knapsack strategy without weights. The kicker here is
          that with every instruction picked, the remaining list must be sorted again

        """

        n = len(s)
        m = len(s[0])
        cache = [0] * m

        # calc initial values and create new list of 2 tuples
        t = []
        for instruction in s:
            k = 0
            for c instruction:
                if c == 1:
                    k += 1
            t.append((instruction, int(math.pow(k, 2))))

        # sort the new tuple list and run through knapsack
        sorted_t = _sort_instructions(t, cache)

        return knapsack(sorted_t, cache, m)


    def knapsack(self, sv, cache, m):
        if m == 0: return 0

        # make new list without mth_item and sort it
        sv2 = list(sv)
        mth_item, mth_val = sv[m - 1]
        sv2.remove((mth_item, mth_val))
        
        # make new cache with the mth_item's 1s ticked off
        cache2 = list(cache)
        for i, c in mth_item:
            if c == '1':
                cache2[i] = 1

        sv2 = self._sort_instructions(sv2, cache2)        

        # return max of mth_item included vs mth_item skipped
        return max(mth_val + self.knapsack(sv2, cache2, m - 1),
                   self.knapsack(sv, cache, m - 1))


    def _sort_instructions(self, t, cache):
        """ Descending order. Returns a list of 2-tuples of """
        new_t = []  # size of t
        j = 0
        for instruction, val in t:
            k = 0
            for i, c in enumerate(instruction):
                if c == '1' and cache[i] != 1: 
                    k += 1
            new_t.append((instruction, int(math.pow(k, 2))))
            j += 1

        return sorted(new_t, lambda x: x[1], reverse=True)


if __name__ == '__main__':
    s = ""
    OrderOfOperations().minTime()