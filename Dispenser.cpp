/*
 * Dispenser.cpp
 *
 *  Created on: Sep 19, 2015
 *      Author: NitishMohan
 */
#include <stdlib.h>
#include <assert.h>
#include <iostream>

using namespace std;
/// <summary>
/// Facilitates dispensing stamps for a postage stamp machine.
/// </summary>
class StampDispenser
{
private:


public:
	const int *m_stampDenominations;
		size_t m_numStampDenominations;
	StampDispenser();
    /// <summary>
    /// Initializes a new instance of the <see cref="StampDispenser"/> class that will be
    /// able to dispense the given types of stamps.
    /// </summary>
    /// <param name="stampDenominations">
    /// The values of the types of stamps that the machine has.
    /// Should be sorted in descending order and contain at least a 1.
    /// </param>
    /// <param name="numStampDenominations">
    /// The number of types of stamps in the stampDenominations array.
    /// </param>
    StampDispenser(const int* stampDenominations, size_t numStampDenominations);

    /// <summary>
    /// Returns the minimum number of stamps that the machine can dispense to
    /// fill the given request.
    /// </summary>
    /// <param name="request">
    /// The total value of the stamps to be dispensed.
    /// </param>
    /// <returns>
    /// The minimum number of stamps needed to fill the given request.
    /// </returns>
    int CalcNumStampsToFillRequest(int request);
    int min(int a, int b);
};
StampDispenser::StampDispenser(const int* stampDenominations, size_t numStampDenominations) {
	this->m_stampDenominations = stampDenominations;
	this->m_numStampDenominations = numStampDenominations;
}

int StampDispenser::CalcNumStampsToFillRequest(int request) {

	int C[request+1];
	C[0] = 0;
	int min;

	for (int i=1; i <= request; i++)
	{
		min = 999;
		for (int j = 0; j<m_numStampDenominations; j++)
		{
			if ((m_stampDenominations[j] <= i) && (min > C[i-m_stampDenominations[j]]+1))
			{
				min = C[i-m_stampDenominations[j]]+1;
			}
		}
		C[i] = min;
	}
	return C[request];
}

int main()
{
    int stampDenominations[] = {90, 30, 24, 10, 6, 2, 1};
    StampDispenser stampDispenser(stampDenominations, 7);
    cout << "The number of stamps is" <<stampDispenser.CalcNumStampsToFillRequest(18)<< endl;
    assert(stampDispenser.CalcNumStampsToFillRequest(18) == 3);
/*
    // Wrong input
        assert(stampDispenser.CalcNumStampsToFillRequest(-10) == -1);
        assert(stampDispenser.CalcNumStampsToFillRequest(-1) == -1);
        assert(stampDispenser.CalcNumStampsToFillRequest(0) == 0);

        // Additional tests
        assert(stampDispenser.CalcNumStampsToFillRequest(1) == 1);
        assert(stampDispenser.CalcNumStampsToFillRequest(2) == 1);
        assert(stampDispenser.CalcNumStampsToFillRequest(5) == 3);
        assert(stampDispenser.CalcNumStampsToFillRequest(34) == 2);
        assert(stampDispenser.CalcNumStampsToFillRequest(72) == 3);
*/
    return 0;
}




