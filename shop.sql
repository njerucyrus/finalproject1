BEGIN;
--
-- Create model Contact
--
CREATE TABLE "shop_contact" ("id" serial NOT NULL PRIMARY KEY, "phone_number" varchar(13) NOT NULL, "full_name" varchar(100) NOT NULL, "location" varchar(100) NOT NULL);
--
-- Create model Fish
--
CREATE TABLE "shop_fish" ("id" serial NOT NULL PRIMARY KEY, "fish_category" varchar(20) NOT NULL UNIQUE, "photo" varchar(100) NOT NULL);
--
-- Create model Seller
--
CREATE TABLE "shop_seller" ("id" serial NOT NULL PRIMARY KEY, "seller_phone" varchar(13) NOT NULL, "quantity" numeric(4, 2) NOT NULL, "fish_id" integer NOT NULL UNIQUE, "fish_category_id" integer NOT NULL);
CREATE INDEX "shop_fish_fish_category_2aae6389_like" ON "shop_fish" ("fish_category" varchar_pattern_ops);
ALTER TABLE "shop_seller" ADD CONSTRAINT "shop_seller_fish_id_8f04119d_fk_shop_fish_id" FOREIGN KEY ("fish_id") REFERENCES "shop_fish" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shop_seller" ADD CONSTRAINT "shop_seller_fish_category_id_80625e9d_fk_shop_fish_id" FOREIGN KEY ("fish_category_id") REFERENCES "shop_fish" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "shop_seller_e9280c62" ON "shop_seller" ("fish_category_id");

COMMIT;
