class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letter_position = {}
        labels = [[]]

        # record positions of every letter
        for index in range(len(S)):
            if not letter_position.__contains__(S[index]):
                letter_position[S[index]] = [index]
            else:
                letter_position[S[index]].append(index)
        
        # partition
        for index in range(len(S)):
            labels[len(labels)-1].append(S[index])
            letter_position[S[index]].pop(0)

            # if there is no more letter, cut it
            if self.check(labels[len(labels)-1], letter_position):
                labels.append([])
        
        labels.pop()
        return list(map(len, labels))
        

    def check(self, letters, letter_pos):
        for letter in letters:
            if len(letter_pos[letter]) != 0:
                return False
        return True