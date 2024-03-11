from odoo.tests import TransactionCase

class TestCustomProduct(TransactionCase):
    def test_compute_slug(self):
        # Test case for computing slug
        product = self.env['product.template'].create({'name': 'Test Product'})
        self.assertEqual(product.slug, 'test-product', "Slug should be computed based on product name")
    
    def test_additional_barcode_unique_constraint(self):
        # Test case for unique constraint on additional barcode
        product1 = self.env['product.template'].create({'name': 'Product 1', 'additional_barcode': '123'})
        product2 = self.env['product.template'].create({'name': 'Product 2', 'additional_barcode': '123'})
        with self.assertRaises(Exception) as context:
            product2.write({'additional_barcode': '123'})
        self.assertTrue('already exists' in str(context.exception), "Should raise exception for non-unique additional barcode")
