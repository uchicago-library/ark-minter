import json, unittest, urllib.parse, urllib.request

class TestArkValidator(unittest.TestCase):
    def test_valid_arks(self):
        for ark in [
            "ark:61001/b2vj4gw8jr5r", "ark:61001/b23h7q044950",
            "ark:61001/b2zr4r08717m", "ark:61001/b2vq1gh7nr8c",
            "ark:61001/b2wc9qd2mt7g", "ark:61001/b2f84sq5vx6f",
            "ark:61001/b2801q33b980", "ark:61001/b2zq0vv4r749",
            "ark:61001/b2bw1623pt2s", "ark:61001/b2t149p1zz2j",
            "ark:61001/b2663p73kq6r", "ark:61001/b29836t54h3s",
            "ark:61001/b20f1pf5mb56", "ark:61001/b2pn6hd1g12z",
            "ark:61001/b2xd2sq0ms9t", "ark:61001/b2jt8d73jg6p",
            "ark:61001/b2338zn5c639", "ark:61001/b2sj7xw5rf2d",
            "ark:61001/b2wm0bb3m29q", "ark:61001/b2xf22w75t82",
            "ark:61001/b2wg3286s20f", "ark:61001/b23d3j40pt54",
            "ark:61001/b2pp1412zm84", "ark:61001/b2mt3fh2f42x",
            "ark:61001/b2f443n7sv0c", "ark:61001/b23q0q01bc8p",
            "ark:61001/b2gx3ns0pj44", "ark:61001/b29r3mg77d60",
            "ark:61001/b2j777s2rx4v", "ark:61001/b26f9zd3vv4x",
            "ark:61001/b2br3d86f145", "ark:61001/b2mv1gd3vw29",
            "ark:61001/b2rz72v2j48c", "ark:61001/b2k39jm6fz9n",
            "ark:61001/b2vz3gk7fc02", "ark:61001/b27m67f2q751",
            "ark:61001/b2jb1cx2241p", "ark:61001/b2ts4m884v84",
            "ark:61001/b2pt5q35qr4v", "ark:61001/b28q7wh4kf7s",
            "ark:61001/b27c7jx9q987", "ark:61001/b2kd3pn8qq11",
            "ark:61001/b2qf3b896p8n", "ark:61001/b27v2f30xh76",
            "ark:61001/b2sm00m5c222", "ark:61001/b2wn4417833k",
            "ark:61001/b2hs73w8v39r", "ark:61001/b22x89p7415q",
            "ark:61001/b2sk2g57q16s", "ark:61001/b2v288c0hp79",
            "ark:61001/b25s72d46k70", "ark:61001/b2dv2562c254",
            "ark:61001/b2nh2289hm2b", "ark:61001/b21b40g45m8g",
            "ark:61001/b2tj1zx8q26s", "ark:61001/b2vj8kr75j23",
            "ark:61001/b29604m28h1c", "ark:61001/b2gx27x62322",
            "ark:61001/b2px5vw2dc96", "ark:61001/b2fc4pr1sd5k",
            "ark:61001/b2v35n78q15n", "ark:61001/b2xb0ht5r581",
            "ark:61001/b2k44rw0fx7h", "ark:61001/b2tk9t95qj57",
            "ark:61001/b21m2qx8tj8j", "ark:61001/b20m84t7942f",
            "ark:61001/b2rw49f8wr0t", "ark:61001/b2v58ns2qv0w",
            "ark:61001/b27w0tp0s614", "ark:61001/b2nd27g49r0m",
            "ark:61001/b2s97wf8wp08", "ark:61001/b2ts6qt0rr61",
            "ark:61001/b2891g16wr0p", "ark:61001/b2jq6wz8sx8h",
            "ark:61001/b2k66937gk22", "ark:61001/b2114536g84w",
            "ark:61001/b2pd4b376n7c", "ark:61001/b2t42c072g02",
            "ark:61001/b2vc5xg73r90", "ark:61001/b2dh9m321f96",
            "ark:61001/b2dx1408t25h", "ark:61001/b2b28bm7km24",
            "ark:61001/b2zv1sb04f1w", "ark:61001/b2s98b66zj0n",
            "ark:61001/b28t8sj4585v", "ark:61001/b2t05950k05s",
            "ark:61001/b2j060q5m66h", "ark:61001/b2qj9gv7rd11",
            "ark:61001/b2n74dv1zq35", "ark:61001/b2h25dr1qq14",
            "ark:61001/b2070hx4nv9w", "ark:61001/b2654k084728",
            "ark:61001/b2nm90t7gx5g", "ark:61001/b22k30w2vs7b",
            "ark:61001/b2q38mw6dx8x", "ark:61001/b2sd51h9fw93",
            "ark:61001/b2280h81ns13", "ark:61001/b2h59x373q18",
            "ark:61001/b2896ms0xz9w", "ark:61001/b2k17z28t54t"
        ]:
            u = 'http://127.0.0.1:5000/validate?id={}'.format(
                urllib.parse.quote_plus(ark)
            )
            response = json.loads(
                urllib.request.urlopen(u).read().decode('utf-8')
            )
            self.assertEqual(response[ark], 'valid')


if __name__ == '__main__':
    unittest.main()
