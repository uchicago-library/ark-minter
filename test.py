import json, unittest, urllib.parse, urllib.request
from ark_minter import ARKMinter

class TestArkMinter(unittest.TestCase):
    def test_extended_digits(self):
        minter = ARKMinter()

        self.assertEqual(len(minter.extended_digits), 29)
        for c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            self.assertTrue(c in minter.extended_digits)
        for c in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'):
            self.assertTrue(c in minter.extended_digits)
        for c in ('a', 'e', 'i', 'l', 'o', 'u', 'y'):
            self.assertFalse(c in minter.extended_digits)
        
    def test_check_digit(self):
        minter = ARKMinter()

        # John Kunze verified that these ARKs are valid independently on Feb 9, 2022.
        for ark in [
            'ark:61001/b2pf6550897w',
            'ark:61001/b28f3v417d34',
            'ark:61001/b2t23pp5jm2q',
            'ark:61001/b2nx7rm2g21b',
            'ark:61001/b2wg40s1fp6w',
            'ark:61001/b2fh2wx5857n',
            'ark:61001/b2qz7xp4396b',
            'ark:61001/b2d06jp9v056',
            'ark:61001/b27s04v1q626',
            'ark:61001/b2s74f62848j',
            'ark:61001/b2hm89x3kp2k',
            'ark:61001/b27w9wf0t01j',
            'ark:61001/b2jm3bj49j2m',
            'ark:61001/b28420p08725',
            'ark:61001/b2cn01j4sr6f',
            'ark:61001/b20r1290pz26',
            'ark:61001/b2nj62m5g18w',
            'ark:61001/b2vz5xr15j40',
            'ark:61001/b28m12x7hn3s',
            'ark:61001/b2zh79b1fz92',
            'ark:61001/b23t63j4q41w',
            'ark:61001/b24v1fk3dt7n',
            'ark:61001/b2db5fs4256d',
            'ark:61001/b2z384b9fk8f',
            'ark:61001/b27k4dw6ng8q',
            'ark:61001/b21394k7rx6m',
            'ark:61001/b2t17012r92s',
            'ark:61001/b2cw0bc3bh8f',
            'ark:61001/b24h4fw3j46t',
            'ark:61001/b2vk6xj9fz2b',
            'ark:61001/b21v44g08w8z',
            'ark:61001/b2tj6846bp6c',
            'ark:61001/b2h76md33z1m',
            'ark:61001/b2s643f6347z',
            'ark:61001/b2k599f0zp22',
            'ark:61001/b24p1tn7dn5c',
            'ark:61001/b21z7ck6bx1r',
            'ark:61001/b2kn9nz4r74k',
            'ark:61001/b2wm74x3m272',
            'ark:61001/b2037v43v34m',
            'ark:61001/b2128q51c51w',
            'ark:61001/b2146c911z5b',
            'ark:61001/b2sq5n248p2q',
            'ark:61001/b2xf3p404x9q',
            'ark:61001/b26p1rp81q3b',
            'ark:61001/b2qg5vx5c346',
            'ark:61001/b2rr6zj0x23p',
            'ark:61001/b2450wg6zg13',
            'ark:61001/b25v7bk1d14k',
            'ark:61001/b27q1nd0n282',
            'ark:61001/b2b26xj8290p',
            'ark:61001/b24t0510w451',
            'ark:61001/b2b95107m39j',
            'ark:61001/b2584gb4260s',
            'ark:61001/b2fw1ft0f13z',
            'ark:61001/b2js67f2r40v',
            'ark:61001/b2sb2p26zq8k',
            'ark:61001/b2sv5w61rq97',
            'ark:61001/b20x4hb3hr6s',
            'ark:61001/b26s1n801s6r',
            'ark:61001/b20d0461ww78',
            'ark:61001/b2n08bx71669',
            'ark:61001/b22p7611vw9j',
            'ark:61001/b2059hh16189',
            'ark:61001/b2kx28p7sf9r',
            'ark:61001/b2g24pk1wv0k',
            'ark:61001/b2k46cd3vm4x',
            'ark:61001/b2xb3992gf5f',
            'ark:61001/b2qf00w8960w',
            'ark:61001/b2t06m682b9z',
            'ark:61001/b22v83522z5j',
            'ark:61001/b2cw5zd5sp6h',
            'ark:61001/b28d9fq4ws2g',
            'ark:61001/b2t70x49cf0f',
            'ark:61001/b2pk4tp3kd5p',
            'ark:61001/b2t614r86b80',
            'ark:61001/b29p82m41s53',
            'ark:61001/b2314t79688t',
            'ark:61001/b27d3k24vx39',
            'ark:61001/b2s02t205h98',
            'ark:61001/b23m53t9b44h',
            'ark:61001/b24g2tn46763',
            'ark:61001/b2j63kt6825f',
            'ark:61001/b2163bt4207w',
            'ark:61001/b26g84f87003',
            'ark:61001/b2nt1jj0mg0s',
            'ark:61001/b2956nz2k67s',
            'ark:61001/b27d0kk86q48',
            'ark:61001/b2fv6mr1kn2k',
            'ark:61001/b2vn3498fb2t',
            'ark:61001/b2dt0dn37f04',
            'ark:61001/b2519f41fz39',
            'ark:61001/b2vs3x34pp75',
            'ark:61001/b20w3xt6v67p',
            'ark:61001/b2gg1g662n8j',
            'ark:61001/b2q12fh1p389',
            'ark:61001/b26j8n85bb4q',
            'ark:61001/b2fm71x6164w',
            'ark:61001/b2tq48f87p56',
            'ark:61001/b2r28j64dh3f'
        ]:
            self.assertTrue(minter.validate(ark))

if __name__ == '__main__':
    unittest.main()
