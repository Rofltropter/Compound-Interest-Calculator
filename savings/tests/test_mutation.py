import pytest
from interest_calculator.schema import schema
from graphene.test import Client
#from .initialize import initialize

pytestmark = pytest.mark.django_db


def test_mutation_create_savings(snapshot):
    client = Client(schema)
    #executed = client.execute()
    snapshot.assert_match(
        client.execute(
            '''
            mutation createSavings(paymentFrequency: 12, initialDeposit: 1000, monthlyDeposit: 100, interestRate: 0.04){
            savings {
                id
                paymentFrequency
                initialDeposit
                monthlyDeposit
                interestRate
            }
        }
    }
    '''
        ))
