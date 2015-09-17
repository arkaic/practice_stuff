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

        """

        cache = [0] * len(s[0])

        # calc initial values and create new list of 2 tuples
        init_inst_vals = []
        for instruction in s:
            k = 0
            for c in instruction:
                if c == 1:
                    k += 1
            init_inst_vals.append((instruction, int(math.pow(k, 2))))

        # sort the new tuple list and run through dp()
        sorted_inst_vals = self._sort_instructions(init_inst_vals, cache)
        print("Initial sorted_inst_vals: \n{}\n\n".format(sorted_inst_vals))

        order = []

        self.dp(sorted_inst_vals, cache, order, 0)
        return (self.global_best_order, self.global_best_val)


    global_best_val = None
    global_best_order = None
    def dp(self, inst_vals, cache, order, running_val):
        """
        @param inst_vals = [ (str inst, int val), .... ]
        @param order     = [ (str inst, int val), .... ]
        """

        if self.global_best_val is not None and running_val > self.global_best_val:
            return

        # Automatically add in all zero-instructions
        while inst_vals[0][1] == 0:
            order.append(inst_vals.pop(0))

        # Update global bests when all instructions added if values are lower, 
        # or if it's first value
        if not inst_vals:
            if self.global_best_val is None or running_val < self.global_best_val:
                self.global_best_val = running_val
                self.global_best_order = order
            return

        if len(inst_vals) == 1:
            running_val += inst_vals[0][1]
            if self.global_best_val is None or running_val < self.global_best_val:
                self.global_best_val = running_val
                order.append(inst_vals.pop())
                self.global_best_order = order
            return

        lowest = inst_vals[0][1]
        for inst, val in inst_vals:
            if val > lowest:
                break

            clone_instvals = list(inst_vals)
            clone_cache = list(cache)
            clone_order = list(order)

            # Remove instruction, update clonecache, add to cloneorder
            clone_instvals.remove((inst,val))
            for i, c in enumerate(inst):
                if c == '1' and clone_cache[i] != 1:
                    clone_cache[i] = 1
            clone_order.append((inst, val))
            
            print("cloneorder={}".format(clone_order))
            print("cloneinstvalsbefore={}".format(clone_instvals))
            print("clonecachebefore={}".format(clone_cache))
            clone_instvals = self._sort_instructions(clone_instvals, clone_cache)
            print("cloneinstvalsafter= {}".format(clone_instvals))
            print("clonecachebefore={}".format(clone_cache))
            self.dp(clone_instvals, clone_cache, clone_order, running_val + val)

    def _sort_instructions(self, inst_vals, cache):        
        """ @param inst_vals: [ (str instruction, int val) ]
        Ascending order. """
        if not inst_vals: 
            raise Exception("shouldn't happen")
        new_instvals = []  # size of inst_vals
        for i, inst_val in enumerate(inst_vals):
            instruction, val = inst_val
            print(instruction)
            k = 0
            for i, c in enumerate(instruction):
                if c == '1' and cache[i] != 1:
                    k += 1
            new_instvals.append((instruction, int(math.pow(k, 2))))

        return sorted(new_instvals, key=lambda x: x[1])


if __name__ == '__main__':
    s = ["111",
         "010",
         "001"]
    answer = OrderOfOperations().minTime(s)

    print("\n\nINPUT\n{}\n\nANSWER\nOrder: {}\nValue: {}".format(s, answer[0], answer[1]))