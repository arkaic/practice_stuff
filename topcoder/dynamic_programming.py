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
          - Intuitively, we want every new memory access to be as minimal as
            possible
            per instruction
          - Initially, every instruction will be at their maximum values. With 
            each one taken, the rest's values will decrease.
            - all-zero instructions will cost nothing at all times. single-1's
              will always cost 1 or zero. 
              Is it ever justified to choose a two-1 in order to make a single-1
              0? That means take a value hit of 4 over taking a 2 for the two 
              singles
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
            for c in instruction:
                if c == 1:
                    k += 1
            t.append((instruction, int(math.pow(k, 2))))

        # sort the new tuple list and run through dp()
        sorted_t = self._sort_instructions(t, cache)
        print("Initial sorted_t: \n{}\n\n".format(sorted_t))

        order = []
        return self.dp(sorted_t, cache, m, order)

    global_best_value = None

    def dp(self, inst_vals, cache, order):
        """
        @param inst_vals = [ (string instruction, int val), ....]
        @param order = [ (string instruction, int val), .... ] (value of inst)
        """

        # while sv[0][1] == 0:
        #     order.append(sv.pop(0))
        # if not sv:
        #     return (order, 0)
        # if len(sv) == 1:
        #     inst, val = sv.pop()
        #     order.append((inst, val))
        #     return (order, val)

        # # for each instruction that has the lowest value so far
        # lowest = sv[0][1]
        # choices = []
        # for inst, val in sv:
        #     if val > lowest:
        #         break
        #     # clone sv, remove this inst,val from the clone, and re-sort the clone
        #     # with a clone of the cache. The clone cache should be modified too.
        #     clonesv = list(sv)
        #     clonesv.remove((inst,val))
        #     clonecache = list(cache)
        #     clonesv = self._sort_instructions(clonesv, clonecache)
        #     cloneorder = list(order)
        #     cloneorder.append((inst,val))
        #     dp_order, dp_val = self.dp(clonesv, clonecache, cloneorder)
        #     running_val = val + dp_val
        #     choices.append((clonesv, clonecache, dp_order, running_val))
        # best_choices = self._best(choices)
        # if len(best_choices) == 1:
        #     return (best_choices[2], best_choices[3])
        # else:
        #     pass


    def _sort_instructions(self, inst_vals, cache):        
        """ @param inst_vals: [ (str instruction, int val) ]
        Ascending order. """
        if not inst_vals: return inst_vals
        new_instvals = []  # size of inst_vals
        for i, tpl in enumerate(inst_vals):
            instruction, val = tpl
            k = 0
            for i, c in enumerate(instruction):
                if c == '1' and cache[i] != 1: 
                    k += 1
            new_instvals.append((instruction, int(math.pow(k, 2))))

        return sorted(new_instvals, key=lambda x: x[1])

    def _best(self, choices):
        lowest = None
        if len(choices) = 1:
            return choices
        for choice in choices:
            if lowest is None:
                lowest = choice[3]
            elif choice[3] < lowest:
                lowest = choice[3]
        best_choices = []
        for choice in choices:
            if choice[3] == lowest:
                best_choices.append(choice)
        return best_choices


if __name__ == '__main__':
    s = ["111",
         "010",
         "001"]
    answer = OrderOfOperations().minTime(s)

    print("\n\nanswer\n{}".format(answer))