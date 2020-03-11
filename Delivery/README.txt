README

Delivery ms - the delivery hub pushing orders to the drivers
Driver ms - represents an individual driver
Order trigger ms - temporary ms to simulate pushing of orders to the delivery ms

Sequence of starting:
First open the delivery ms.
Then open as many instances of driver ms as you want. Pls note you can only login with DriverIDs already present in the delivery schema.
Then open order trigger to start sending orders.

You can actually open it in other sequence as the messages are persistent. But the above order is easier to understand.

any questions pls ask Sue-Anne.