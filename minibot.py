from multiprocessing import Process, Queue
from time import time

def recproc(rq, s):
	times = []
	while True:
		data = rq.get()
		if data > 0:
			times.append(time() - data)
		else:
			avg = sum(times) / len(times)
			mini = min(times)
			maxi = max(times)
			s.put(f'average time: {avg}, min time: {mini}, max time: {maxi}')
			break
		
if __name__ == '__main__':
	q = Queue()
	s = Queue()
	p = Process(target=recproc, args=(q,s,))
	p.start()
	start = time()
	print(f'start time: {start}')
	for x in range(1000000):
		q.put(time())
	q.put(-1)
	x = s.get()
	print(x)
	stop = time()
	print(f'stop time: {stop}')
	print('total time: {:.4}'.format(stop-start))
	p.terminate()