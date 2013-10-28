Title: Rolling on IPv6
Date: 2011-07-29 10:09
Author: rav
Category: Uncategorized
Slug: rolling-on-ipv6

As we all should know, our traditional [IPv4] addresses are being
rapidly depleted. But, not to fear, [IPv6][]was designed to succeed the
old system and provide with at almost limitless supply of new addresses
as well as new changes to the way the Internet communications stack
works. The transition from IPv4 to IPv6 will be gradual but 6sync have
now taken our first steps toward this by rolling out IPv6 connectivity!

Each 6sync client will now receive access to an entire IPv6 /64 block
which will provide 18,446,744,073,709,551,616 (18 quintillion) addresses
that can be used! And yes, that is more addresses than what is available
in the entire IPv4 space :-) You can assign these addresses amongst your
biscuits any way you wish.

*How do I get it?!* Addresses have already been assigned to most clients
and you can find it under the IP Addressing section of Biscuit. If you
don't see your allocation there yet don't worry,.. a few people will
have to wait a weeee bit longer and we will email those affected (Sorry
guys!)

**EDIT: check out the new [IPv6 setup guide][]!**

*How do I use it?!* Currently we are not using the auto-configuration
feature of IPv6 so you must manually choose and configure all your
addresses. We have some more detailed guides about how to do this on the
way, for now something like:

    sudo ip -6 addr add 2605:4500:xxxx:xxxx::yyyy/64 dev eth0

will work! (Remember to replace xxxx with your assigned IP block and
yyyy with a natural number like '6' or '123')

*Is it working?!* Best way to check is to ping someone..

    ping6 ipv6.google.com

if you get a response back then all is well, congratulations.

  [IPv6]: http://en.wikipedia.org/wiki/IPv6
  [IPv6 setup guide]: http://articles.6sync.com/documentation/configure-an-ipv6-address
