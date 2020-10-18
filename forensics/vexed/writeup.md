# Vexed Solution

From the title "vexed", I was hoping they would pick up on "vexillology" (the study of flags).

Looking at packets 95-244, they show some strange TCP packets with all different flags that you normally would not get if it was normal traffic.
```
196	31.799073077	127.0.0.1	127.0.0.1	TCP	54	[TCP Out-Of-Order] 5432 → 2345 [SYN, PSH, URG, CWR] Seq=0 Win=1505 Urg=0 Len=0
197	31.799081924	127.0.0.1	127.0.0.1	TCP	54	2345 → 5432 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
198	31.799121747	127.0.0.1	127.0.0.1	TCP	54	[TCP Retransmission] 5432 → 2345 [SYN, RST, CWR] Seq=0 Win=1505 Len=0
```

If you look at TCP data for the packets in Wireshark, it displays the flags nicely like:
```
...0 .... .... = Nonce: Not set
.... 1... .... = Congestion Window Reduced (CWR): Set
.... .0.. .... = ECN-Echo: Not set
.... ..0. .... = Urgent: Not set
.... ...0 .... = Acknowledgment: Not set
.... .... 0... = Push: Not set
.... .... .1.. = Reset: Set
.... .... ..1. = Syn: Set
.... .... ...0 = Fin: Not set
```

As you look at more packets in this area of the pcap, you can see that the NONCE and FIN flag are never set, only the middle 7 bits.

If you copy the exact order of the and flags and decode it from binary, you would see a 'C' for the first packet.
Then looking at the next one, you would see a 'U', so on and so on.

You could easily solve the challenge with something like scapy as I showed in solve.py.

I would say it is a little guessy, but you usually never see flags used in the way they are used in the packet capture for TCP data.
