# questo e' praticamente un M/M/2 tipo .. solo che la coda e' formata da due utenti
# il secondo arriva un secondo dopo
# il numero di risorse sono appunto due, il tempo di servizio e' fissato a 5 per semplicita'

# import random
import simpy

INTERVAL_CUSTOMERS = 0.0  # Generate new customers roughly every x seconds


def source(env, numeroClienti, interval, counter):
    c = customer(env, 'Customer1', counter, time_in_bank=12.0)
    env.process(c)
    t = 1  # indica in pratica dopo quanto puo' arrivare quello dopo
    yield env.timeout(t)  # e' praticamente ogni quanto arrivano

    c = customer(env, 'Customer2', counter, time_in_bank=12.0)
    env.process(c)
    t = 0  # infatti in questo caso lui arriva un secondo dopo
    yield env.timeout(t)  # e' praticamente ogni quanto arrivano


def customer(env, name, counter, time_in_bank):
    """Customer arrives, is served and leaves."""
    arrive = env.now
    print('%7.4f %s: Here I am' % (arrive, name))

    with counter.request() as req:
        # Wait for the counter or abort at the end of our tether
        yield req

        wait = env.now - arrive

        # We got to the counter
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))

        tib = 5  # random.expovariate(1.0 / time_in_bank)  # tempo di servizio
        print("tempo di servizio %s" % tib)
        yield env.timeout(tib)
        print('%7.4f %s: Finished' % (env.now, name))


env = simpy.Environment()
counter = simpy.Resource(env, capacity=2)  # counter dovrebbe essere il tipo di risorsa
env.process(source(env, 2, INTERVAL_CUSTOMERS, counter))
env.run()
