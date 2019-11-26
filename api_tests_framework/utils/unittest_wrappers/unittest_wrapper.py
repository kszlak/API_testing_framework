from unittest import TestCase


class ModelValidationTestCase(TestCase):
    def assertModel(self, model, model_type):
        self.assertTrue(model["createdAt"])
        self.assertTrue( model["updatedAt"])
        self.assertTrue( model["id"])
        self.assertEqual( model["modelType"], model_type )

    def assertUserModel(self, model):
        # Check if keys exists (double checking)
        """self.assertIn( "createdAt", model )
        self.assertIn( "updatedAt", model )
        self.assertIn( "id", model )
        self.assertIn( "modelType", model )
        self.assertIn( "username", model )
        self.assertIn( "firstname", model )
        self.assertIn( "lastname", model )"""

        self.assertModel(model=model, model_type="UserModel")

        # Check if is not none
        self.assertTrue( model["username"] )
        self.assertTrue( model["firstname"] )
        self.assertTrue( model["lastname"] )

    def assertThreadModel(self, model):
        self.assertModel( model=model, model_type="ThreadModel" )

        self.assertTrue( model["name"] )
        self.assertTrue( model["owner"] )
        self.assertTrue( model["user"] )
        self.assertIsNotNone( model["private"] )
        #different example of validation
        #self.assertIn(model["private"], [True, False])
        #self.assertIsInstance(model["private"], bool)
        self.assertIsNotNone( model["deleted"] )

    def assertUsernameValidationModel(self, model):
        self.assertModel( model=model, model_type="UsernameValidationModel" )

        self.assertIsNotNone( model["errors"] )











