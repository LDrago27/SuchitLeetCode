from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        ctr = Counter(senate)
        # While banning each will try to ban an opposite closest to them else the other guy can ban someone from his party
        
        n = len(senate)
        
        senate = list(senate)
        
        skipD, skipR = 0,0
        
        
        
        while senate:
            
            newSenate = []    
            for ele in senate:
                
                if ele == 'R':
                    
                    if skipR <= 0:
                    
                        # read it 
                        newSenate.append('R')

                        #remove a D
                        ctr['D'] -=1
                        skipD +=1
                    else:
                        skipR -=1
                        
                else:
                    
                    if skipD <=0:
                        # read it 
                        newSenate.append('D')

                        #remove a R
                        ctr['R'] -=1
                        skipR +=1
                    else:
                        skipD -=1
                        
                if ctr['D'] <=0:
                    return 'Radiant'
                if ctr['R']<=0:
                    return 'Dire'
                
            senate = newSenate
                    
                        
            
            
            
            
            
        