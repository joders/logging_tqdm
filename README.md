# logging_tqdm
Include the last state of your tqdm status bar into your log

This code was designed with the goal of keeping the tqdm usage the same. Only the import has to be changed from "from tqdm import tqdm" to "from logging_tqdm import tqdm". The logging api is called transparently in the background.

Depending on the information you print when using your logger you will get a log like this:

2017-12-28 17:01:18,317:    100%|██████████| 100/100 [00:02<00:00, 49.48it/s]



When an exception is being thrown during the iteration, logging_tqdm logs the status state when the exception occurred. In the case of a simple iteration wrapped by tqdm, e.g. "for i in tqdm(range(10)):" the logs will look something like the following when encountering an exception:

2017-12-31 09:27:12,173:    failed on item: 75
2017-12-31 09:27:12,174:     75%|███████▌  | 75/100 [00:01<00:00, 49.46it/s]



In the more complicated case of using tqdm with pandas (progress-apply) we get a similar output except when an exception is thrown. Unfortunately the looks of the status bar can not be recovered but a log informs about the index of the item that the iteration failed on:

2017-12-31 09:27:14,412:    Failed on pandas apply during the 7. invocation of the provided apply function processing item: 
     classes      data
1          5 -0.584023
17         5  1.111667
33         5  1.577957
...

Running test.py you can replicate the output above.

One last note: This is not an all powerful python package but only a piece of code you will most likely have to adopt to your needs (such as connecting it to the logger you use in your application). Only the test/demonstration (test.py) should work out of the box.

